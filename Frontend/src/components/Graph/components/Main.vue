<template>
    <div class="main_container">
        <div class="main_dir">
            <span class="dir_root">我的文件</span>
            <span class="icons el-icon-menu"></span>
            <span class="icons el-icon-sort"></span>
            <span class="icons el-icon-search"></span>
        </div>
        <div class="main_content">
            <div class="nofiles">
                <img src="../../../assets/images/empty_file.png" alt="">
                <div>当前文件夹没有文件</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.main_container{
    height: calc(100% - 51px);
    /* min-width: 320px; */
    position: relative;
    z-index: 1;
    padding-left: 20px;
}
.main_dir{
    box-sizing: content-box;
    height: 28px;
    line-height: 28px;
    color: #666;
    font-size: 12px;
    position: relative;
    padding-top: 16px;
}
.main_dir .dir_root{
    padding-left: 0;
    color: #666;
    font-weight: 400;
    cursor: default;
    vertical-align: middle;
}
.main_dir .icons{
    font-size: 18px;
    cursor: pointer;
    float: right;
    margin-right: 20px;
    vertical-align: -3px;
    color: #666;
    line-height: 26px;
}
.main_content{
    overflow-y: scroll;
    padding-top: 13px;
    width: 100%;
}
.main_content .nofiles{
    margin: 230px auto;
    font-size: 15px;
    text-align: center;
    color: #999;
}
</style>