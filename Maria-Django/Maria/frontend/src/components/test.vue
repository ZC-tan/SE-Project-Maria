<template>
  <editor v-model="content"></editor>
</template>

<script>
import Editor from "./tinymce_editor.vue"
export default {
  name: "test",
  components: {
    Editor
  },
  data(){
    return{
      isShow:false,
      content:'your content'
    }
  }
}
</script>

<style scoped>

</style>