<template>
  <div class="_nav">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">Akash's Blog</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item active-class="active" :to="{name: 'Home'}" exact>Home</b-nav-item>
          <b-nav-item active-class="active" :to="{name: 'BlogList'}">Blog</b-nav-item>
          <b-nav-item href="#">About</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<style>
  ._nav{
    width:100%;
  }
</style>
