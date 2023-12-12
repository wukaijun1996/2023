<template>
  <div class="home">
    <h1>主页</h1>
    {{ a }}
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data: function () {
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
  components: {}
}
</script>
