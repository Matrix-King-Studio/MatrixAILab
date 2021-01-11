<template>
    <div class="header_container">
        <div class="header_left">
            <router-link to="/">
                <img width="35px" height="35px" src="../../../assets/logo.png" alt="">
            </router-link>
            <router-view></router-view>
        </div>
        <div class="header_center">
            <span>团队 
                <i class="el-icon-arrow-down"></i>
            </span>
            <span><router-link to="/graph" class="nav nav_active">个人</router-link></span>
            <span><router-link to="/graph/recommend" class="nav">推荐</router-link></span>
            <span><router-link to="/graph/template" class="nav">模板</router-link></span>
        </div>
        <div class="header_right">
            <div class="user_logo" :style="{'borderColor':show ? '#ccc' : 'transparent'}" @click.stop="showmenu">
                <img :src="user_img" alt="">
            </div>
           
        </div>
         <ul class="user_menu" v-show="show" ref="showPanel">
            <li>
                <router-link to="/graph" class="nav">
                    <span class="icon el-icon-folder"></span>
                    个人文件
                </router-link>
            </li>
            <li class="sep"></li>
            <li v-for="(item,index) in userlist" :key="index+'1'">
                <router-link to="" class="nav">
                    <span :class="item.icon"></span>
                    {{item.name}}
                </router-link>
            </li>
            <li class="sep"></li>
            <li>
                <router-link to="/logout" class="nav">
                    <span class="iconfont icon-logout-- icon"></span>
                    退出登录
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user_img:require('@/assets/logo.png'),
            userlist:[
                {
                    name:'账户中心',
                    icon:"iconfont icon-zhanghuzhongxinmoren"
                },
                {
                    name:'个人主页',
                    icon:"iconfont icon-gerenzhuye"
                },
                {
                    name:'交易记录',
                    icon:"iconfont icon-jiaoyijilu"
                },
                {
                    name:'偏好设置',
                    icon:"iconfont icon-shezhi-copy"
                },
                {
                    name:'入门教程',
                    icon:"iconfont icon-wenhao"
                },
                {
                    name:'新功能',
                    icon:"iconfont icon-update"
                }
            ],
            show:false,
        }
    },
    created(){
        //设置点击user_logo以外的地方时，隐藏user_menu盒子
        document.addEventListener('click',(e)=>{
            if(this.$refs.showPanel){
                let isSelf = this.$refs.showPanel.contains(e.target);
                if(!isSelf){
                    this.show = false
                }
            }
        })
    },
    methods:{
        showmenu() {
            if(!this.show) this.show=true;
        },
    }
}
</script>

<style scoped>
.header_container{
    position: relative;
    display: flex;
    height: 50px;
    width: 100%;
    line-height: 50px;
    padding: 0 40px;
    background-color: #fff;
    border-bottom: 1px solid #e5e5e5;
    box-shadow: 0 3px 2px -2px rgba(200,200,200,.1);
    justify-content: space-between;
}
.header_left{
    width: 120px;
}
.header_center{
    flex: 1;
    text-align: center;
    overflow: hidden;
    min-width: 80px;
    padding: 0 8px;
}
.header_center span{
    font-size: 13px;
    margin-right: 35px;
    color: #333;
}
.nav{
    color: #333;
}
.nav_active{
    color: #4386f5 !important;
}
.header_center:nth-child(4){
    margin-right: 0;
    margin-left: 34px;
}
.header_right {
    position: relative;
    width: 120px;
}
.header_right .user_logo{
    position: absolute;
    right: -5px;
    top: 5px;
    cursor: pointer;
    border: 5px solid transparent;
    border-radius: 50%;
}
.header_right .user_logo:hover{
    border: 5px solid #ccc;
}
.header_right .user_logo img {
    width: 30px;
    height: 30px;
    display: block;
    border-radius: 50%;
    cursor: pointer;
}
.user_menu{
    position: absolute;
    width: 140px;
    z-index: 2;
    top: 45px;
    right: 20px;
    display: block;
    padding: 8px 0;
    min-width: 160px;
    background: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 1px 6px #ccc;
    border-radius: 3px;
    margin-top: 4px;
}
.user_menu li {
    padding: 7px 12px;
    cursor: default;
    color: #444;
    line-height: 20px;
    position: relative;
    display: flex;
    align-items: center;
    font-size:12px ;
}
.user_menu li:hover{
    background: #f5f5f5;
    color: #000;
}
.user_menu li span {
    display: inline-block;
    vertical-align: middle;
    margin: -1px 6px 0 0;
    font-size: 14px;
}
.user_menu li.sep{
    margin: 3px 0;
    padding: 0;
    height: 1px;
    width: 100%;
    background-color: #e7e7e7;
}
</style>