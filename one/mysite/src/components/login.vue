<template>
    <div>
      <h1>用户登陆</h1>
      <input type="text" placeholder="用户名" v-model="username">
      <input type="text" v-model = "password">
      <input type="button" v-on:click=" doLogin">

    </div>
</template>

<script>
    export default {
        name: "login",
      data(){
          return {
            username:'',
            password:'',
          }
      },
      methods:{
          doLogin:function(){
            //向你的后端发送ajax请求
            this.$axios.request({
              url: "",
              method:"POST",
              data:{
                user:this.username,
                pwd:this.password,
              },
              headers:{  //告诉你的后端你发送的数据类型
                'Content-Type:':'application/json'
              },
              responseType:"json"
            }).then(function(arg){
              //成功了
              console.log(123);
            }).catch(function(arg){
                consloe.log("失败了")
            })
          }
      }
    }
</script>

<style scoped>

</style>
