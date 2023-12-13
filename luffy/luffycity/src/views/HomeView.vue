<template>
  <div class="home">
    <Head></Head>
    <Banner></Banner>
    <Footer></Footer>
  </div>
</template>

<script>
  //导入头部组件
  import Head from "@/components/Head";
  import Footer from "@/components/Footer";
  import Banner from "@/components/Banner";
  export default {
    name: 'HomeView',
    data() {
      return {a: 123}
    },
    created() {
      //向后端发请求
      //es5
      // this.$axios.get('http://127.0.0.1:8081/home/home/').then(function (response) {
      //   console.log(response.data)
      // }).catch(function (error) {
      //   console.log(error)
      // }),
      //es6的箭头函数
      this.$axios.get('http://127.0.0.1:8081/home/home/').then(
          response => {
            console.log(response.data)
          }
      ).catch(error => {
        console.log(error.date)
      })
    },

    components: {
      Head,
      Footer,
      Banner,
    }
  }
</script>
