<template>
  <div id="header">
    <nav class="navbar navbar-expand-lg bg-white navbar-light shadow sticky-top p-0">
      <router-link to="/" class="navbar-brand d-flex align-items-center px-4 px-lg-5">
        <h2 class="m-0 fw-semi-bold logo"><i class="fa fa-book me-3"></i>vnEdu Clone App</h2>
      </router-link>

      <b-navbar-toggle target="navbar-toggle-collapse">
        <template #default="{ expanded }">
          <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
          <b-icon v-else icon="chevron-bar-down"></b-icon>
        </template>
      </b-navbar-toggle>

      <b-collapse id="navbar-toggle-collapse" is-nav>
        <b-navbar-nav class="ml-auto ms-auto">
          <router-link to="/" class="nav-item nav-link active">Trang chủ</router-link>
          <router-link to="/scores" class="nav-item nav-link">Xem điểm</router-link>
          <router-link to="/users" class="nav-item nav-link">Tôi</router-link>
        </b-navbar-nav>
        <router-link to="/admin" class="btn btn-primary py-4 px-lg-5 d-none d-lg-block .fw-medium rounded-0">Quản trị</router-link>
      </b-collapse>

    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "HeaderMenu",
  data() {

  },
}
</script>

<style>

/*** Navbar ***/
.navbar-light .navbar-nav .nav-link {
  margin-right: 30px;
  padding: 25px 0;
  color: #FFFFFF;
  text-transform: uppercase;
  outline: none;
}

.navbar-light .navbar-nav .nav-link:hover,
.navbar-light .navbar-nav .nav-link.active {
    color: var(--primary);
}

@media (max-width: 991.98px) {
    .navbar-light .navbar-nav .nav-link  {
        margin-right: 0;
        padding: 10px 0;
    }

    .navbar-light .navbar-nav {
        border-top: 1px solid #EEEEEE;
    }
}

.navbar-light .navbar-brand,
.navbar-light a.btn {
    height: 75px;
}

.navbar-light .navbar-nav .nav-link {
    color: var(--dark);
    font-weight: 500;
}

.navbar-light.sticky-top {
    top: -100px;
    transition: .5s;
}

.logo {
  color: var(--primary);
}

</style>
