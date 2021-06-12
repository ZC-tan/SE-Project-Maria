<template>
  <div>
    <form action="" class="login">
      <p>Login</p>
      <input type="text" placeholder="用户名">
      <input type="password" placeholder="密码">
      <input type="submit" class="btn" value="登  录">&nbsp;&nbsp;&nbsp;
      <router-link to="login/register">
        <input class="btn" value="  注  册">
      </router-link>
    </form>
  </div>
</template>

<script>
export default {
  name: "login"
}
</script>

<style >

</style>
