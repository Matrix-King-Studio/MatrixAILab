<template>
  <a-page-header class="header"
    style="border: 1px solid rgb(235, 237, 240);"
    :title="projectName"
    @back="() => null">
    <template slot="tags">
      <a-tag color="blue">
        Running
      </a-tag>
    </template>
    <div class="login_box">
        <router-link class="login" to="/login">
          <el-button size="small" class="login_btn" type="primary">登录</el-button>
        </router-link>
        <router-link class="register" to="/register">
          <el-button size="small" class="register_btn" type="primary">注册</el-button>
        </router-link>
    </div>
  </a-page-header>
</template>

<script>
import project from "@/config/api/project";
import {mapGetters} from "vuex";

export default {
  name: "Header",
  data() {
    return {
      projectName: "",
    }
  },
  computed: {
    ...mapGetters(["graphId"]),
  },
  created() {
    this.init()
  },
  methods: {
    init() {
      project.getProjectInfo(1).then(res => {
        this.projectName = res.data.name
      }).catch(err => {
        console.log(err);
      })
    }
  }
}
</script>

<style scoped>
.header{
  position: relative;
}
.login_box{
  position: absolute;
  right: 40px;
  top: 16px;
}
.login,
.register {
  color: #fff;
}
.login .login_btn,
.register .register_btn{
  margin-left: 10px;
}
</style>