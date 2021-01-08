<template>
    <div class="login_container">
        <div class="login_box">
            <!-- 头像区域 -->
            <div class="avatar_box">
                <img src="../assets/logo.png" alt="">
            </div>
            <!-- 注册按钮 -->
            <div class="register">
                <span>没有账号?</span>
                <router-link class="register_btn" to="/register">立即注册</router-link>
            </div>
            <!-- 登录表单区域 -->
            <el-form ref="loginFormRef" :rules="loginFormRules" label-width="0px" class="login_form" :model="loginForm">
                <!-- 用户名 -->
                <el-form-item prop="username">
                    <el-input v-model="loginForm.username" prefix-icon="iconfont icon-user"></el-input>
                </el-form-item>
                <!-- 密码 -->
                <el-form-item prop="password">
                    <el-input v-model="loginForm.password" prefix-icon="iconfont icon-3702mima" type="password"></el-input>
                </el-form-item>
                <!-- 按钮区域 -->
                <el-form-item class="btns">
                    <el-button @click="login" type="primary">登录</el-button>
                    <el-button type="info">
                        <router-link class="forgetpass" to="/forgetpass">忘记密码</router-link>
                    </el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>
<script>
import userApi from '@/config/api/user'
export default {
    data() {
        return {
            // 登录表单的数据绑定对象
            loginForm:{
                username:'',
                password:''
            },
            // 表单的验证规则对象
            loginFormRules:{
                // 验证用户名
                username:[
                    {require:true,message:"请输入用户名",trigger:"blur"},
                    {min:2,max:10,message:"长度在 2 到 10 个字符之间",trigger:"blur"}
                ],
                // 验证密码
                password:[
                    {require:true,message:"请输入密码",trigger:"blur"},
                    {min:6,max:15,message:"长度在 6 到 15 个字符之间",trigger:"blur"}
                ]
            }
        }
    },
    methods:{
        login() {
            this.$refs.loginFormRef.validate(async valid =>{
                // if(!valid) return;
                // const{data:res}= this.$axios.post('admin',this.loginForm);
                // if(res.meta.status!=200) return this.$message.error('登录失败！');
                // this.$message.success('登录成功！');
                userApi.login(id).then(res=>{
                    console.log(res);
                }).catch(err=>{ // eslint-disable-line no-unused-vars
                    console.log(err);
                });
            }) 
        }
    }
}
</script>
<style scoped>
.login_container{
    height: 100%;
    background-color: #2b4b6b;
}
.login_box{
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
.login_box .avatar_box{
    height: 130px;
    width: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;    
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%,-50%);
    background-color: #fff;
}
.login_box .avatar_box img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #eee;
}
.login_form{
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
}
.btns{
    display: flex;
    justify-content: flex-end;
}
.forgetpass{
    color: #fff;
}
.register{
    position: absolute;
    right: 15px;
    top: 20px;
}
.register .register_btn{
    color: red;
}
</style>