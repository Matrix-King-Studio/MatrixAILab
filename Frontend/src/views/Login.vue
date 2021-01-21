<template>
    <div class="login_container">
        <div class="login_box">
            <!-- 头像区域 -->
            <div class="avatar_box">
                <img src="../assets/logo.png" alt="">
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
                <el-form-item prop="status">
                    <JcRange :status="status" @Cstatus="Cstatus"></JcRange>
                </el-form-item>
                <!-- 按钮区域 -->
                <el-form-item class="btns">
                    <el-button class="login_btn" @click="login" type="primary">登录</el-button>
                </el-form-item>
            </el-form>
            <div class="option">
                <el-button class="forgetpass" size="small">
                    <router-link class="forgetpass_btn" to="/forgetpass">忘记密码</router-link>
                </el-button>
                <el-button size="small" class="register">
                    <router-link class="register_btn" to="/register">立即注册</router-link>
                </el-button>
            </div>
        </div>
    </div>
</template>
<script>
import userApi from '@/config/api/user'
import JcRange from '@/components/public/JcRange.vue'

export default {
    data() {
        var checkStatus = (rule, value, callback) => {
            if (this.status == false) {
                return callback(new Error("请拖动滑块完成验证"));
            } else {
                callback();
            }
        };
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
                    {required:true,message:"请输入用户名",trigger:"blur"},
                    {min:2,max:10,message:"长度在 2 到 10 个字符之间",trigger:"blur"}
                ],
                // 验证密码
                password:[
                    {required:true,message:"请输入密码",trigger:"blur"},
                    {min:6,max:15,message:"长度在 6 到 15 个字符之间",trigger:"blur"}
                ],
                status:[{validator: checkStatus, trigger: "change" }],
                
            },
            status:false
        }
    },
    components: {
		JcRange
	},
    methods:{
        login() {
            this.$refs.loginFormRef.validate(async valid =>{
                // if(!valid) return;
                // const{data:res}= this.$axios.post('admin',this.loginForm);
                // if(res.meta.status!=200) return this.$message.error('登录失败！');
                // this.$message.success('登录成功！');
                // userApi.login(id).then(res=>{
                //     console.log(res);
                // }).catch(err=>{ // eslint-disable-line no-unused-vars
                //     console.log(err);
                // });
            }) 
        },
        Cstatus(data){
            this.status=data;
        }
    },
}
</script>
<style scoped>
.login_container{
    height: 100%;
    background-image: url('../assets/login/bg.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
}
.login_box{
    width: 450px;
    height: 370px;
    background-color: rgb(247,249,251);
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
    background-color: rgb(247,249,251);
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
    margin-bottom: 35px;
}
.btns{
    margin-top: 10px;
    width: 100%;
}
.btns .login_btn{
    width: 100%;
}
.option{
    width: 100%;
    height: 40px;
    position: absolute;
    bottom: 5px;
    padding: 0 20px;
}
.forgetpass{
    float: right;
    
}
.forgetpass .forgetpass_btn{
    color:skyblue;
}
.register{
    float: left;
    margin-left: 0px !important;
}
.register .register_btn{
    color:skyblue;   
}
</style>