<template>
  <div>
    <form action="" class="register">
      <p>register</p>
      <input type="text" placeholder="用户名">
      <input type="password" placeholder="密码">
      <input type="text" placeholder="手机号码"></input>
      <input type="text" placeholder="邮箱"></input>
      <input type="submit" class="btn" value="注  册">
    </form>
  </div>
</template>

<script>
export default {
  name: "login"
}
</script>

<style >
.login_container{
  background-color: #2b4b6b;
  height: 100%;
}
.login_box{
  width: 450px;
  height: 300px;
  background-color: plum;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
}
</style>
