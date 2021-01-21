<template>
    <div class="main">
        <div class="bars_des">
            <span class="filecount">
                文件数
                <span>{{filesCount}}</span>
                /
                <span>9</span>
            </span>
            <a href="#" :style="{'color':'#444'}" class="right">升级</a>
        </div>
        <div class="bars">
            <div class="bars_before" :style="{'width':bars_width}"></div>
        </div>
        <a href="#" class="bars_des_bt">免费增加文件数</a>
    </div>
</template>

<script>
export default {
    data() {
        return {
            bars_width:0,
        }
    },
    computed:{
        filesCount:function(){
            return this.$store.state.graphFilesCount
        }
    },
    methods:{
        filesbar(){
            var rate=this.filesCount/9*100;
            this.bars_width=rate+'%'
        }
    },
    mounted(){
        this.filesbar()
    }
}
</script>

<style scoped>
.main{
    position: relative;
}
.bars_des{
    position: absolute;
    left: 0;
    top: -22px;
    z-index: 2;
    font-size: 12px;
    color: #666;
    display: block;
    width: 100%;
}
.bars{
    height: 8px;
    border: 1px solid #ddd;
    border-radius: 2px;
}
.bars .bars_before{
    position: absolute;
    left: 0;
    transition: width .5s;
    top: 0;
    z-index: 2;
    height: 8px;
    background: #4386f5;
    border: 1px solid #4386f5;
    border-radius: 2px;
    max-width: 175px;
}
.bars_des_bt{
    font-size: 12px;
    color: #aaa;
    margin-top: 4px;
    display: block;
}
</style>