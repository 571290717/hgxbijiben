Page({
  data:{
      hello:"Hi",
  },
  change: function(){
      this.setData({
          hello : this.data.hello + "~~~`",
      })
  },
});