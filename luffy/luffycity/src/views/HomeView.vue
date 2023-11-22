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
    return {'a': 123}
  },
  components: {}
}
</script>
