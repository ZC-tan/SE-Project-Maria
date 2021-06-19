<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <span>玛丽亚线上文档</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <el-menu background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" :router="true"
                 default-active="$router.path">
            <el-menu-item index="/user">
              <span slot="title">个人资料</span>
            </el-menu-item>
            <el-menu-item index="/创建文档">
              <span slot="title">创建文档</span>
            </el-menu-item>
          <el-menu-item index="/自己创建的文档">
            <span slot="title">自己创建的文档</span>
          </el-menu-item>
          <el-menu-item index="/favorites" >
            <span slot="title">收藏文档</span>
          </el-menu-item>
            <el-menu-item index="/team">
              <span slot="title">查看团队</span>
            </el-menu-item>
          <el-menu-item index="/最近浏览的文档">
            <span slot="title">最近浏览的文档</span>
          </el-menu-item>
          <el-menu-item index="/回收箱">
            <span slot="title">回收箱</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <!-- 右侧内容主体 -->
      <el-main>
        <!-- 路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  created() {
    this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    logout() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    // 获取所有的菜单
    async getMenuList() {
      const { data: res } = await this.$http.get('menus')
      if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
      this.menulist = res.data
      console.log(res)
    },
    // 点击按钮，切换菜单的折叠与展开
    toggleCollapse() {
      this.isCollapse = !this.isCollapse
    },
    // 保存链接的激活状态
    saveNavState(activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    }
  }
}
</script>

<style lang="less" scoped>
.home-container {
  height: 950px;
}
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #fff;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}

.el-aside {
  background-color: #333744;
  .el-menu {
    border-right: none;
  }
}

.el-main {
  background-color: #eaedf1;
}

.iconfont {
  margin-right: 10px;
}

.toggle-button {
  background-color: #4a5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
  cursor: pointer;
}

html,body,#app{
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>
