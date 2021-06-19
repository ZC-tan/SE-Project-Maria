<template>
  <div>
    <el-breadcrumb separator="">
      <el-breadcrumb-item :to="{ path: '/firstpage' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/"></a></el-breadcrumb-item>
      <el-breadcrumb-item></el-breadcrumb-item>
      <el-breadcrumb-item></el-breadcrumb-item>
    </el-breadcrumb>
    <el-card >
      <el-row>
        <el-col :span="8">
          <el-input placeholder="请输入文档名称或id" v-model="input" clearable>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary">搜索文档</el-button>
        </el-col>
      </el-row>
      <el-table
          :data="tableData"
          style="width: 100%">
        <el-table-column
            prop="id"
            label="文档id"
            width="400">
        </el-table-column>
        <el-table-column
            prop="name"
            label="文档名称"
            width="400">
        </el-table-column>
        <el-table-column
            prop="power"
            label="收藏日期"
            width="450">
        </el-table-column>
      </el-table>
    </el-card>

  </div>
</template>

<script>

</script>

<style>

</style>