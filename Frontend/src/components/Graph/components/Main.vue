<template>
    <div class="main_container">
        <div class="main_dir">
            <span class="dir_root">我的文件</span>
            <span class="icons el-icon-menu"></span>
            <span class="icons el-icon-sort"></span>
            <span class="icons el-icon-search"></span>
        </div>
        <div class="main_content">
            <div class="nofiles" style="display:none">
                <img src="../../../assets/images/empty_file.png" alt="">
                <div>当前文件夹没有文件</div>
            </div>
            <div class="files_list_title">
                文件
            </div>
            <div class="files_list_item" v-for="(item,index) in fileslist" :key="index+'2'">
                <div class="file_img">
                    <img :src="item.img" alt="">
                </div>
                <div class="title">
                    <a href="#">
                        <span id="icons" class="icon" :class="item.icon" style="color: #4386f5;font-size: 17px;"></span>
                        <label>{{item.name}}</label>
                    </a>
                </div>
            </div>   
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return{
            fileslist:[
                {
                    name:'file1',
                    icon:'icon-update',
                    img:require('@/assets/images/file1.jpg')
                },
                {
                    name:'file2',
                    icon:'icon-update',
                    img:require('@/assets/images/file2.jpg')
                },
                {
                    name:'file3',
                    icon:'icon-update',
                    img:require('@/assets/images/file3.jpg')
                },
            ],
        }
    },
    computed:{
        listlength:function(){
            return this.fileslist.length;
        }
    },
    methods:{
        filesLength(data){
            this.$store.commit({
                type:'filesCount',
                count:data
            });
        }
    },
    created(){
        this.filesLength(this.listlength)

    }
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
.files_list_title{
    font-size: 12px;
    color: #aaa;
    margin-top: -4px;
    margin-bottom: 8px;
}
.files_list_item{
    width: calc(20% - 16px);
    min-height: 130px;
    vertical-align: top;
    position: relative;
    display: inline-block;
    border-radius: 3px;
    min-width: 130px;
    max-width: 200px;
    margin-right: 16px;
    margin-bottom: 15px;
    transition: all .4s;
    z-index: 1;
}
.files_list_item .file_img{
    position: relative;
}
.files_list_item .file_img img{
    display: block;
    min-height: 173px;
    height: 100%;
    width: 100%;
    border-radius: 5px;
    border: 1px solid #e6e6e6;
    box-shadow: 0 1px 1px 0 rgba(0,0,0,.2);
    border-bottom: 0;
}
.files_list_item .title{
    text-align: left;
    padding-left: 2px;
    display: block;
    /* text-align: center; */
    font-size: 12px;
    margin-top: 4px;
    line-height: 16px;
    max-height: 32px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
.files_list_item .title a{
    color: #333;
    font-size: 13px;
}
.files_list_item .title a #icons{
    margin-right: 6px;
    vertical-align: -1px;
}
.files_list_item .title a label{
    cursor: pointer;
}
</style>