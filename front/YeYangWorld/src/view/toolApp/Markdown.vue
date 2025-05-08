<template>

    <header class="header">

        <navigate></navigate>


        <div class="nav">

            <router-link class="return" to="/toolbegin">返回</router-link>

            <div class="name">markdown编辑器</div>

            <el-button class="upload" @click="upload = !upload">上传</el-button>

        </div>

    </header>


    <input class="title" placeholder="请输入标题" v-model="title"></input>


    <div id="vditor"></div>


    <el-dialog v-model="upload" title="上传文章" width="50%" center>
        <el-form :model="form" label-width="120px">
            <el-form-item label="文章分类"></el-form-item>
            <el-form-item label="文章封面">
                <el-upload action="your-upload-url" list-type="picture-card" :auto-upload="false"
                    :show-file-list="false" :limit="1" :on-change="handleChange" :handleRemove="handleremove"
                    :file-list="fileList">
                    <el-icon v-if="!imageUrl">
                        <Plus />
                    </el-icon>
                    <img class="img" v-if="imageUrl" :src="imageUrl" />
                    <el-icon class='delete' v-if="imageUrl" @click="deleteimg">
                        <DeleteFilled />
                    </el-icon>
                </el-upload>
            </el-form-item>
        </el-form>
        <template #footer>
            <el-button @click="upload = false">取 消</el-button>
            <el-button type="primary" @click="certainupload">确定上传</el-button>
        </template>
    </el-dialog>

</template>



<script setup>
import { ref, onMounted, inject } from 'vue';
import Vditor from 'vditor'
import 'vditor/dist/index.css';
const axios = inject('axios')

//markdown编辑器
const vditor = ref()
function creatVditor() {
    vditor.value = new Vditor('vditor', {
        width: '900px',
        height: '580px',
    })
}
onMounted(creatVditor)


//显示图片
const imageUrl = ref('')
function handleChange(uploadFile) {
    imageUrl.value = URL.createObjectURL(uploadFile.raw);
    fileList.value.push(uploadFile.raw)
    console.log(fileList.value)
}
//删除图片
const fileList = ref([])
function deleteimg() {
    imageUrl.value = ''
    console.log(fileList.value)
    fileList.value = []
}


const upload = ref(false)
const title = ref('')
const content = ref('')
const category_id = ref('')
async function certainupload() {
    content.value = vditor.value.getHTML()
    console.log(content.value)
    // 创建一个新的FormData对象
    const formData = new FormData();
    // 向FormData对象中添加字段
    formData.append('title', title.value);
    formData.append('cover', fileList.value[0]); 
    formData.append('category_id', category_id.value);
    formData.append('content', content.value);
    const response = await axios.post('/read/upload_article/', formData)
    console.log(response.data)
}


</script>


<style scoped>
.header {
    width: 100%;
    display: flex;
    flex-direction: column;
}

.nav {
    width: 100%;
    display: flex;
    flex-direction: row;
    background-color: #f7efef;
    justify-content: space-between;
    font-size: 25px;
    color: #f12222;

}

.title {
    width: 1225px;
    height: 50px;
    font-size: 30px;
    color: #000000;
    font-weight: bold;

}

.img {
    width: 100%;
    height: 100%;
    border-radius: 10px;
}

.delete {
    position: absolute;
    top: 0;
    left: 150px;

}
</style>