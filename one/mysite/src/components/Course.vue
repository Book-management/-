<template>
  <div>
    <h1>课程列表</h1>

    <ul v-for="item in courseList">
      <li>{{ item.name}}</li>

    </ul>

  </div>
</template>

<script>
export default {
name: "course",
  data(){
    return {
      courseList :[
        {id:1,title:"python基础"},
        {id:2, title:"java基础"},
        {id:3,title:"js基础"},
        {id:4, title:"C#基础"}
      ]
    }
  },
  mounted(){  //当你的页面挂载之后 开始加载数据的时候先执行它
  this.initCourse();   //调用你的methods中定义的方法
  },

  methods:{
    initCourse:function(){
      var that = this;
      //向后台发送请求
      this.$axios.request({
        url:"http://127.0.0.1:8000/api/course/",  //后端请求的路径
        method:"GET",
        responseType:"json",
      }).then(function(arg){
        //成功之后
        that.courseList = arg.data.data

      })
    }

  }


}
</script>

<style scoped>

</style>
