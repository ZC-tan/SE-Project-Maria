<!--<template>-->
<!--  <div class="tinymce-editor">-->
<!--    <editor-->
<!--        v-model="myValue"-->
<!--        :init="init"-->
<!--        :disabled="disabled"-->
<!--        @onClick="onClick">-->
<!--    </editor>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--import tinymce from 'tinymce/tinymce'-->
<!--import Editor from '@tinymce/tinymce-vue'-->
<!--import 'tinymce/themes/silver/theme'-->
<!--// 更多插件参考：https://www.tiny.cloud/docs/plugins/-->
<!--import 'tinymce/plugins/image'// 插入上传图片插件-->
<!--// import 'tinymce/plugins/media'// 插入视频插件-->
<!--import 'tinymce/plugins/table'// 插入表格插件-->
<!--// import 'tinymce/plugins/lists'// 列表插件-->
<!--import 'tinymce/plugins/wordcount'// 字数统计插件-->
<!--import 'tinymce/plugins/paste';//复制粘贴图片-->
<!--import 'tinymce/plugins/fullscreen';//全屏插件-->
<!--export default {-->
<!--  components: {-->
<!--    Editor-->
<!--  },-->
<!--  props: {-->
<!--    //传入的默认值-->
<!--    value: {-->
<!--      type: String,-->
<!--      default: ''-->
<!--    },-->
<!--    //是否禁用-->
<!--    disabled: {-->
<!--      type: Boolean,-->
<!--      default: false-->
<!--    },-->
<!--    //插件-->
<!--    plugins: {-->
<!--      type: [String, Array],-->
<!--      default: 'image table wordcount paste fullscreen'-->
<!--    },-->
<!--    //菜单-->
<!--    toolbar: {-->
<!--      type: [String, Array],-->
<!--      //如果显示的内容和配置的不符，表明插件未引入。需要去引入插件；-->
<!--      default: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media fullpage | forecolor backcolor emoticons | help'-->
<!--    },-->
<!--    //编辑器高度-->
<!--    height:{-->
<!--      default:300-->
<!--    }-->
<!--  },-->
<!--  data () {-->
<!--    let _this = this;-->
<!--    return {-->
<!--      init: {-->
<!--        language_url: '/static/tinymce/lang/zh_CN.js',  //中文包路径地址-->
<!--        language: 'zh_CN',-->
<!--        skin_url: '/static/tinymce/skins/ui/oxide', //皮肤包路径地址-->
<!--        height: this.height,//编辑器高度-->
<!--        max_height:570,//resize为true时，控制编辑器的最大高度-->
<!--        plugins: this.disabled?'':this.plugins,  // 插件-->
<!--        toolbar: this.disabled?'':this.toolbar,  // 工具栏-->
<!--        images_upload_url: '', //上传路径-->
<!--        elementpath:false,//标签路径是否显示-->
<!--        menubar:false,//顶部菜单-->
<!--        resize:this.disabled?false:true,//页面大小拖动-->
<!--        paste_data_images: true,//可以粘贴图片，需要引入paste插件-->
<!--        content_style:'div,p{margin:5px 0;}'+'img{max-width:100%;}'+'*::-webkit-scrollbar{width:6px;height:6px;background:transparent;}'+'*::-webkit-scrollbar-thumb{border-radius: 3px;background: #bac3d9;}',-->
<!--        // 此处为图片上传处理函数，这个直接用了base64的图片形式上传图片-->
<!--        // 直接使用base64处理，最好还是上传到服务器，因为base64存储到服务器数据库太庞大了-->
<!--        images_upload_handler: (blobInfo, success, failure) => {-->
<!--          const img = 'data:image/jpeg;base64,' + blobInfo.base64()-->
<!--          success(img)-->
<!--        },-->
<!--        init_instance_callback : function(editor) {-->
<!--          _this.editorId = editor.id;-->
<!--        },-->
<!--        branding:false-->
<!--      },-->
<!--      myValue: this.value,-->
<!--      editorId:null-->
<!--    }-->
<!--  },-->
<!--  mounted () {-->
<!--    tinymce.init({})-->
<!--  },-->
<!--  methods: {-->
<!--    onClick (e) {-->
<!--      this.$emit('onClick', e, tinymce)-->
<!--    }-->
<!--  },-->
<!--  watch: {-->
<!--    value (newValue) {-->
<!--      this.myValue = newValue-->
<!--    },-->
<!--    myValue (newValue) {-->
<!--      this.$emit('input', newValue)-->
<!--    }-->
<!--  }-->
<!--}-->

<!--</script>-->


<!--作者：解八哥-->
<!--链接：https://juejin.cn/post/6844904070218530829-->
<!--来源：掘金-->
<!--著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。-->