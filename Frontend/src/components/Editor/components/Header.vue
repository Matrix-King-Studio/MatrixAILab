<template>
  <a-page-header class="header"
    style="border: 1px solid rgb(235, 237, 240);"
    :title="projectName"
    @back="() => this.$router.push('/graph')">
    <template slot="tags">
      <a-tag color="blue">
        Running
      </a-tag>
    </template>
  </a-page-header>
</template>

<script>
import project from "@/config/api/project";
import {mapGetters} from "vuex";

export default {
  name: "Header",
  data() {
    return {
      projectName: "",
    }
  },
  computed: {
    ...mapGetters(["graphId"]),
  },
  created() {
    this.init()
  },
  methods: {
    init() {
      project.getProjectInfo(1).then(res => {
        this.projectName = res.data.name
      }).catch(err => {
        console.log(err);
      })
    }
  }
}
</script>

<style scoped>

</style>