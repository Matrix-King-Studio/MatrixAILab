<template>
  <div>
    <a-drawer
      title="参数设置"
      placement="right"
      :closable="true"
      :width="500"
      :visible="parameterVisible"
      :get-container="false"
      :mask="false"
      :wrap-style="{ position: 'absolute' }"
      @close="onClose">
      <a-form-model
        :model="form"
        :label-col="{span: 5}"
        :wrapper-col="{span: 17}">
        <div
          v-for="parameter in parameters"
          :key="parameter.id">
          <a-tooltip
            placement="left">
            <template slot="title">
              <span>{{ parameter.describe }}</span>
            </template>
            <a-form-model-item
              :label="parameter.name">
              <div v-if="parameter.type.search('str') !== -1">
                <a-input
                  v-model="parameter.value"/>
              </div>
              <div v-else-if="parameter.type.search('int') !== -1">
                <a-input-number
                  v-model="parameter.value"
                  :min="1"
                  :max="10"/>
              </div>
              <div v-else-if="parameter.type.search('file') !== -1">
                <a-select
                  default-value=""
                  style="width: 120px"
                  v-model="parameter.value">
                  <a-select-option
                    v-for="item in fileList"
                    :key="item.id"
                    :value="item.id">
                    {{ item.filename }}
                  </a-select-option>
                </a-select>
                <a-divider
                  type="vertical"/>
                <a-upload
                  name="file"
                  :accept="acceptFile(parameter)"
                  :multiple="true"
                  action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                  :headers="headers"
                  @change="handleChange">
                  <a-button>
                    <a-icon
                      type="upload"/>
                  </a-button>
                </a-upload>
                <a-button
                  v-if="parameter.value"
                  type="primary"
                  @click="showModalAndReadFile(parameter.value)">
                  数据处理
                </a-button>
              </div>
              <div v-else-if="parameter.type.search('bool') !== -1">
                <a-switch
                  checked-children="True"
                  un-checked-children="False"
                  v-model="parameter.value"/>
              </div>
              <div v-else>
                暂不支持
              </div>
            </a-form-model-item>
          </a-tooltip>
        </div>
      </a-form-model>
    </a-drawer>
    <a-modal
      title="数据处理"
      :width="1200"
      :maskClosable="false"
      :visible="dataProcessModalVisible"
      :confirm-loading="confirmLoading"
      @ok="handleOk"
      @cancel="handleCancel">
      <DataProcess :fileId="fileId"></DataProcess>
    </a-modal>
  </div>
</template>

<script>
import DataProcess from "@/components/Editor/components/DataProcess";

export default {
  name: "Parameter",
  components: {
    DataProcess
  },
  props: ["parameterVisible", "parameters", "fileList"],
  data() {
    return {
      fileId: "",
      dataProcessModalVisible: false,
      confirmLoading: false,

      headers: {
        authorization: 'authorization-text',
      },
      form: {
        name: '',
        region: undefined,
        date1: undefined,
        delivery: false,
        type: [],
        resource: '',
        desc: '',
      },
    };
  },
  created() {
    this.init()
  },
  methods: {
    init() {

    },

    acceptFile(parameter) {
      if (parameter.name.search("csv") !== -1) {
        return ".csv"
      } else if (parameter.name.search("json") !== -1) {
        return ".json"
      }
    },

    onClose() {
      this.$emit("closeDrawer")
    },

    handleChange(info) {
      if (info.file.status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (info.file.status === 'done') {
        this.$message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === 'error') {
        this.$message.error(`${info.file.name} file upload failed.`);
      }
    },

    showModalAndReadFile(filePath) {
      this.fileId = filePath
      this.dataProcessModalVisible = true;
    },

    // eslint-disable-next-line no-unused-vars
    handleOk(e) {
      this.ModalText = 'The modal will be closed after two seconds';
      this.confirmLoading = true;
      setTimeout(() => {
        this.dataProcessModalVisible = false;
        this.confirmLoading = false;
      }, 2000);
    },

    // eslint-disable-next-line no-unused-vars
    handleCancel(e) {
      console.log('Clicked cancel button');
      this.dataProcessModalVisible = false;
    },
  }
}
</script>

<style>
div.ant-drawer-body {
  padding: 4px;
  font-size: 14px;
  line-height: 1.5;
  word-wrap: break-word;
}
</style>