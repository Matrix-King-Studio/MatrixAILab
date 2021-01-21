<template>
    <div class="aside_container">
        <div class="container_box">
            <el-button size="small" @click="toggleShow" class="new_file" round>
                <svg class="icon" aria-hidden="true">
                    <use xlink:href="#icon-xinjian"></use>
                </svg>
                新建</el-button>
            <div class="create_list" v-show="isShow">
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-wenjianjia"></use>
                        </svg>
                    </span>
                    <span class="list_text">新建文件夹</span>
                </div>
                <span class="sub"></span>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-daoru"></use>
                        </svg>
                    </span>
                    <span class="list_text">导入</span>
                </div>
                <span class="sub"></span>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-liuchengtu"></use>
                        </svg>
                    </span>
                    <span class="list_text">流程图</span>
                </div>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-siweidaotu"></use>
                        </svg>
                    </span>
                    <span class="list_text">思维导图</span>
                </div>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-bjON"></use>
                        </svg>
                    </span>
                    <span class="list_text">思维笔记</span>
                </div>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-DESIGN_huaban"></use>
                        </svg>
                    </span>
                    <span class="list_text">原型图</span>
                </div>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-curriculum_living"></use>
                        </svg>
                    </span>
                    <span class="list_text">UML</span>
                </div>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-wangluozu"></use>
                        </svg>
                    </span>
                    <span class="list_text">网络拓扑图</span>
                </div>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-zu9999"></use>
                        </svg>
                    </span>
                    <span class="list_text">组织结构图</span>
                </div>
                <div>
                    <span class="icon_box">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#icon-lianjie"></use>
                        </svg>
                    </span>
                    <span class="list_text">BPMN</span>
                </div>
                <router-link class="list_more" to="/graph/template">
                    <span class="list_text">更多图形和模板>></span>
                </router-link>
            </div>
        </div>
        <router-link v-for="(item,index) in navlist" :key="index+'1'" :to="item.router" class="aside_nav" :class="item.class">
            <span :class="item.icon"></span>
            <label>{{item.name}}</label>
        </router-link>
        <div class="bottom_files">
            <bottom-com></bottom-com>
        </div>
    </div>
</template>

<script>
import bottomCom from './Asidebottom'
export default {
    data() {
        return {
            isShow:false,
            navlist:[
                {
                    name:'我的文件',
                    router:'/graph',
                    icon:'el-icon-house',
                    class:'active'
                },
                {
                    name:'最近修改',
                    router:'/graph/history',
                    icon:'el-icon-time',
                    class:''
                },
                {
                    name:'与我协作',
                    router:'/graph/colla',
                    icon:'el-icon-user',
                    class:''
                },
                {
                    name:'我的收藏',
                    router:'/graph/fav',
                    icon:'el-icon-star-off',
                    class:''
                },
                {
                    name:'回收站',
                    router:'/graph/trash',
                    icon:'el-icon-delete',
                    class:''
                },
            ]
        }
    },
    methods: {
        toggleShow() {
            this.isShow=!this.isShow
        }
    },
    components:{
        bottomCom
    }
}
</script>

<style scoped>
.aside_container{
    width: 208px;
    height: calc(100% - 40px);
    position: relative;
}
.container_box .create_list {
    position: fixed;
    top: 100px;
    left: 36px;
    border-radius: 3px;
    /* display: none; */
    box-shadow: 1px 1px 4px #ddd;
    min-height: 370px;
    width: 210px!important;
    background: #fff;
    border: 1px solid #ddd;
    transition: all .2s ease-in-out;
    overflow: hidden;
    text-align: left;
    z-index: 10;
    padding-bottom: 7px;
}
.container_box .create_list div{
    box-sizing: content-box;
    height: 26px;
    padding: 7px 10px;
    line-height: 26px;
    cursor: pointer;
    position: relative;
}
.container_box .create_list div:first-child{
    margin-top: 3px;
}
.container_box .create_list div:hover{
        background: #f5f5f5;
}
.container_box .create_list div .icon_box{
    cursor: pointer;
    height: 24px;
    line-height: 25px;
    width: 24px;
    display: inline-block;
    -moz-border-radius: 50%;
    -webkit-border-radius: 50%;
    border-radius: 50%;
    text-align: center;
    margin: 0 10px 0 0;
}
.container_box .create_list div .list_text {
    display: inline-block;
    vertical-align: 2px;
    font-size: 12px;
    cursor: pointer;
    color: #000;
}
.sub{
    height: 1px;
    background: #eee;
    margin: 2px 0;
    display: block;
}
.container_box .create_list .list_more{
    display: block;
    text-align: center;
    font-size: 13px;
    color: #666;
    cursor: pointer;
    padding: 0px 0px 6px 0px;
    margin-top: 4px;
}
.container_box .new_file{
    margin-left: 36px;
    margin-top: 16px;
    margin-bottom: 6px;
    width: 126px;
}
.aside_container>.aside_nav{
    height: 45px;
    line-height: 45px;
    font-size: 14px;
    text-align: center;
    display: block;
    color: #888;
    width: 140px;
    margin: 0 auto;
}
.aside_container>.aside_nav span{
    font-size: 18px;
    margin-right: 12px;
    vertical-align: -1px;
}
.aside_container>.aside_nav label{
    display: inline-block;
    min-width: 100px;
    text-align: left;
    cursor: pointer;
}
.active{
    font-weight: 700;
    color: #555 !important;
}
.bottom_files{
    position: absolute;
    bottom: 70px;
    left: 18px;
    width: 175px;
    z-index: 2;
}
</style>