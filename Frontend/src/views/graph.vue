<template>
    <el-container>
        <el-header style="height:50px">
            <header-com></header-com>
        </el-header>
        <el-container>
            <el-aside width="208px">
                <aside-com></aside-com>
            </el-aside>
            <el-main>
                <main-com></main-com>
            </el-main>
        </el-container>
</el-container>
</template>

<script>
import headerCom from '@/components/Graph/components/Header';
import asideCom from '@/components/Graph/components/Aside';
import mainCom from '@/components/Graph/components/Main';

export default {
    components:{
        headerCom,
        asideCom,
        mainCom
    }
}
</script>

<style scoped>
.el-header,
.el-aside,
.el-main{
    padding: 0;
}
.el-aside,
.el-main{
    height: 100vh;
    background-color: rgb(244,244,244);
}
</style>