<template>
  <div class="banner">
    <el-carousel  height="400px">
      <el-carousel-item v-for="item in 4" :key="item">
        <img src="@/assets/img/banner1.png" alt="">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "Banner"
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