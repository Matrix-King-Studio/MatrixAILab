<template>
    <div class="register_container">
        <div class="register_box">
            <!-- 头像区域 -->
            <div class="avatar_box">
                <img src="../assets/logo.png" alt="">
            </div>
            <!-- 登录表单区域 -->
            <el-form ref="registerFormRef" status-icon :rules="registerFormRules" label-width="0px" class="register_form" :model="registerForm">
                <!-- 用户名 -->
                <el-form-item prop="username">
                    <el-input  placeholder="请输入用户名" v-model="registerForm.username" prefix-icon="iconfont icon-user"></el-input>
                </el-form-item>
                <!-- 密码 -->
                <el-form-item prop="password">
                    <el-input  placeholder="请输入密码" v-model="registerForm.password" prefix-icon="iconfont icon-3702mima" type="password" autocomplete="off" show-password></el-input>
                </el-form-item>
                <!-- 确认密码 -->
                <el-form-item prop="checkPass">
                    <el-input placeholder="请再次输入密码" v-model="registerForm.checkPass" type="password"  prefix-icon="iconfont icon-3702mima" autocomplete="off" show-password></el-input>
                </el-form-item>
                <!-- 手机号 -->
                <el-form-item prop="phonenum" class="phonenum">
                    <el-input class="phone_input"  placeholder="请输入手机号" prefix-icon="el-icon-mobile-phone" v-model="registerForm.phonenum"></el-input>
                    <el-button type="primary">发送验证码</el-button>
                </el-form-item>
                <!-- 验证码 -->
                <el-form-item prop="checkcode">
                    <el-input placeholder="请输入验证码" v-model="registerForm.checkcode"  prefix-icon="iconfont icon-3702mima" autocomplete="off"></el-input>
                </el-form-item>
                <!-- 按钮区域 -->
                <el-form-item>
                    <el-button class="btns" @click="register" type="primary">注册</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>
<script>
import userApi from '@/config/api/user'
export default {
    data() {
        var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.registerForm.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
        return {
            // 注册表单的数据绑定对象
            registerForm:{
                username:'',
                password:'',
                checkPass:'',
                phonenum:'',
                checkcode:''
            },
            // 表单的验证规则对象
            registerFormRules:{
                // 验证用户名
                username:[
                    {require:true,message:"请输入用户名",trigger:"blur"},
                    {min:2,max:10,message:"长度在 2 到 10 个字符之间",trigger:"blur"}
                ],
                // 验证密码
                password:[
                    {require:true,message:"请输入密码",trigger:"blur"},
                    {min:6,max:15,message:"长度在 6 到 15 个字符之间",trigger:"blur"}
                ],
                //二次密码
                checkPass:[
                   {validator: validatePass2, trigger:'blur' }
                ],
                //验证手机号
                 phonenum:[
                    {require:true,message:"请输入手机号",trigger:"blur"},
                    {min:11,max:11,message:"手机号长度为11位",trigger:"blur"}
                ],
            }
        }
    },
    methods:{
        
    }
}
</script>
<style scoped>
.register_container{
    height: 100%;
    background-color: #2b4b6b;
}
.register_box{
    width: 450px;
    height: 450px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
.register_box .avatar_box{
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
.register_box .avatar_box img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #eee;
}
.register_form{
    position: absolute;
    top: 80px;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
}
.phonenum{
    display: flex;
}
.phonenum .phone_input{
    width: 296px;
}
.btns{
    width: 150px;
    margin-left: 125px;
}
</style>