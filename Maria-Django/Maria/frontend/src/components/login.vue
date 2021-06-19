<template>
  <body class="loginpic">
  <div >
    <form action="" class="login">
      <p>Login</p>
      <input type="text" placeholder="用户名">
      <input type="password" placeholder="密码">
      <router-link to="/firstpage">
        <input class="btn" value="  登  录">
      </router-link>&nbsp;&nbsp;&nbsp;
      <router-link to="/login/register">
        <input class="btn" value="  注  册">
      </router-link>


    </form>
  </div>
  </body>
</template>

<script>

export default {
  name: "login",

}

</script>

<style >
body{
  background-size: cover;
  background: url(wallpaper.jpg) no-repeat fixed;
}
</style>