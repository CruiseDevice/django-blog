<template>
  <div class="container">
    <div class="card">
      <div class="card-body">
        <div class="card-title">
          <h4>{{postById.title}}</h4>
          <footer class="badge"  v-for="tag in postById.tagList" :key="tag.id">
            <span class="badge badge-secondary">{{tag}}</span>
          </footer>
          <small class="text-muted float-right">{{postById.published_date | date}}</small>
        </div>
        <div v-html="postById.text"></div>
      </div>
    </div>
    <div class="commments">
      <div class="card">
        <div class="card-body">
          <div class="card-title">
            <h4>Comments:</h4>
              <div v-for="comments in postById.commentsList" :key="comments.id">
                {{comments.body}}
                <footer class="badge">
                  <span class="badge badge-secondary">by {{comments.name}}</span>
                </footer>
              </div>
          </div>
        </div>
      </div>
    </div>
    <div class="comment-form">
      <CommentComponent/>
    </div>
  </div>
</template>
<script>
import CommentComponent from './CommentComponent'
export default {
  name: 'Post',
  components: {
    CommentComponent
  },
  props: ['post_id'],
  computed: {
    postById () {
      return this.$store.getters.postById(Number(this.post_id))
    }
  }
}
</script>
<style>
  .card {
    margin-top: 2em;
  }
</style>
