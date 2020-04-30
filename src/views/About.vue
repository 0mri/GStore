<template>
  <form @submit.prevent="UpdateEmail" class="section">
    <div class="columns is-centered">
      <div class="column is-4">
        <div class="card">
          <div class="card-content">
            <div
              style="justify-content: center;"
              class="media has-text-centered"
            >
              <div class="media-left">
                <b-field class="file">
                  <b-upload
                    accept="jpg,jpeg,png"
                    @input="UploadImage"
                    :disabled="profileImage != null"
                    drag-drop
                    v-model="profileImage"
                    class="upload"
                    type="is-info"
                  >
                    <figure class="image">
                      <!-- <img
                      class="is-rounded"
                      src="https://bulma.io/images/placeholders/96x96.png"
                      alt="Placeholder image"
                    /> -->
                      <v-lazy-image
                        class="is-rounded image is-128x128"
                        alt="Profile Image"
                        :src="user.profile_image || ''"
                      />
                    </figure>
                  </b-upload>
                </b-field>
                <b-progress
                  v-if="profileImage != null"
                  :value="percentage"
                  show-value
                  format="percent"
                ></b-progress>
                <b-field> </b-field>
                <p class="title is-4">
                  {{ user.username }}
                </p>
              </div>
            </div>
            <div class="media ahi">
              <div class="field">
                <strong>ID</strong>
                <span>{{ `**` }}</span>
              </div>
              <div class="field">
                <strong>From</strong>
                <span>Israel</span>
              </div>
              <div class="field">
                <strong>Member Since</strong>
                <span>{{
                  new Date(user.date_joined).toLocaleDateString('en-GB')
                }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-4">
        <div class="card">
          <div class="card-content">
            <b-field label="First Name">
              <b-input disabled :value="user.first_name" />
            </b-field>
            <b-field label="Last Name">
              <b-input disabled :value="user.last_name" />
            </b-field>
            <div class="field">
              <b-field label="Email">
                <b-field>
                  <div class="input-field">
                    <small v-if="!editEmail"
                      ><a @click.prevent="editEmail = true" class="edit-input"
                        >Edit Email</a
                      ></small
                    >
                    <b-input
                      type="email"
                      required
                      v-model="new_user.email"
                      v-bind:placeholder="
                        !editEmail ? user.email : 'Type your new email'
                      "
                      :disabled="!editEmail"
                    />
                  </div>
                </b-field>
              </b-field>
              <b-field v-if="editEmail">
                <b-input
                  type="email"
                  required
                  placeholder="Confirm your new email"
                />
              </b-field>
            </div>

            <div class="field">
              <b-field label="Password">
                <b-field>
                  <div class="input-field">
                    <small v-if="!editPassword"
                      ><a
                        @click.prevent="editPassword = true"
                        class="edit-input"
                        >Edit Password</a
                      ></small
                    >
                    <b-input
                      v-bind:placeholder="
                        !editPassword ? '*****' : 'Type your old password'
                      "
                      type="password"
                      :disabled="!editPassword"
                    />
                  </div>
                </b-field>
              </b-field>
              <b-field v-if="editPassword">
                <b-input placeholder="Type your new password" type="password" />
              </b-field>
              <b-field v-if="editPassword">
                <b-input
                  placeholder="Confirm your new password"
                  type="password"
                />
              </b-field>
            </div>
          </div>
          <div class="" style="justify-content: center;">
            <div class="card-content">
              <b-field>
                <b-button
                  disabled
                  :loading="formLoading"
                  native-type="submit"
                  type="is-primary is-fullwidth"
                >
                  Update Profile
                </b-button>
              </b-field>
            </div>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import api from '@/services/api'
import { mapState } from 'vuex'
export default {
  name: 'about',
  computed: mapState('User', ['user']),
  data() {
    return {
      loading: true,
      editEmail: false,
      editPassword: false,
      profileImage: null,
      new_user: {
        first_name: '',
        last_name: '',
        email: '',
      },
      formLoading: false,
      percentage: 0,
    }
  },
  mounted() {
    this.loading = false
  },
  methods: {
    UpdateEmail() {
      this.formLoading = true
      axios
        .put('api/auth/users/me/', {
          email: this.email,
        })
        .then(({ data }) => {
          this.$store.dispatch('User/setUser', data)
          this.editEmail = false
          this.email = ''
          this.$buefy.toast.open({
            message: 'Update Success',
            type: 'is-success',
          })
        })
        .catch((err) => {
          // console.log(err)
          // this.$buefy.toast.open({
          //   message: err.response.data.email[0],
          //   position: 'is-right',
          //   type: 'is-danger',
          // })
        })
        .finally(() => {
          this.formLoading = false
        })
    },
    async UploadImage(imageFile) {
      this.percentage = 0
      const reader = new FileReader()
      const oldPhoto = this.user.profile_image
      reader.onload = (e) => {
        this.user.profile_image = e.target.result
      }
      reader.readAsDataURL(this.profileImage)

      this.$store
        .dispatch('User/updateProfileImage', {
          imageFile,
          progress: (progress) => {
            this.percentage = progress
          },
        })
        .then((response) => {
          if (response.status != 200) this.user.profile_image = oldPhoto
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.profileImage = null
        })
    },
  },
}
</script>

<style scoped>
.ahi {
  display: block;
}
span {
  float: right;
}
.input-field {
  position: relative;
}
.edit-input {
  position: absolute;
  z-index: 5;
  right: 1.5rem;
  top: 0.47rem;
}
</style>

<style>
.upload .upload-draggable {
  border-radius: 1000px !important;
}
.upload-draggable.is-info.is-loading::after {
  position: absolute;
  top: calc(50% - 1.5rem);
}
</style>
