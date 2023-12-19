<template>
  <div class="banner">
    <el-carousel height="400px">
      <el-carousel-item v-for="item in banner_list">
        <!--        <img src="@/assets/img/banner1.png" alt="">-->
        <router-link :to="item.link">
          <img :src="item.img" :alt="item.name">
        </router-link>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {
      banner_list: []
    }
  },
  created() {
    // 当banner组件创建，就向后端发请求，拿回轮播图数据
    this.$axios.get(this.$settings.base_url + '/home/banner/').then(response => {
      console.log(response.data)
      this.banner_list = response.data
    }).catch(errors => {
      console.log(errors.data)
    })


  },


}


</script>

<style scoped>


el-carousel-item {
  height: 400px;
  min-width: 1200px;
}

.el-carousel__item img {
  height: 400px;
  margin-left: calc(50% - 1920px / 2);
}
</style>