import api from '@/services/api'

export default {
  async putImage(image, upluadEvent) {
    const formData = new FormData()
    formData.append('file', image)
    return api
      .put('account/profileimage/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        timeout: 1000 * 20,
        onUploadProgress: (uploadEvent) => upluadEvent(uploadEvent),
      })
      .then((response) => response)
      .catch((error) => error)
  },
}
