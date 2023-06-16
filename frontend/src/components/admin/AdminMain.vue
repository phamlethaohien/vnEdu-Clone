<template>
  <div class="admin-main">
    <aside class="left-sidebar">
      <nav class="siderbar-nav scroll-sidebar">
        <ul class="pt-4">
          <li class="sidebar-item">
            <router-link to="/admin/users" class="sidebar-link nav-link active">QUẢN LÝ NGƯỜI DÙNG</router-link>
          </li>
          <li class="sidebar-item">
            <router-link to="/admin/schools" class="sidebar-link nav-link">QUẢN LÝ TRƯỜNG HỌC</router-link>
          </li>
          <li class="sidebar-item">
            <router-link to="/admin/classrooms" class="sidebar-link nav-link">QUẢN LÝ LỚP HỌC</router-link>
          </li>
          <li class="sidebar-item">
            <router-link to="/admin/scores" class="sidebar-link nav-link">QUẢN LÝ ĐIỂM SỐ</router-link>
          </li>
          <li class="sidebar-item">
            <router-link to="/admin/notifications" class="sidebar-link nav-link">QUẢN LÍ THÔNG BÁO</router-link>
          </li>
        </ul>
      </nav>
    </aside>
  </div>
</template>

<script>

export default {
  name: 'AdminMain',
  components: {

  },
  data() {

  },
}
</script>

<style>
.left-sidebar {
  width: 270px;
  height: 100%;
  transition: 0.2s ease-in;
  z-index: 11;
  border-right: 1px solid rgb(229, 234, 239);
  background-color: #fff;
}

.left-sidebar .scroll-sidebar {
  overflow-y: auto;
  padding: 0 18px 0 0;
  height: calc(100vh - 80px);
}

.left-sidebar .sidebar-item {
  line-height: 26px;
  text-transform: uppercase;
}

.left-sidebar .sidebar-item .sidebar-link {
  display: flex;
  align-items: center;
  margin: 0 0 2px;
  padding: 12px;
  border-radius: 7px;
  line-height: 25px;
  font-weight: 500;
  color: #1d1d1d;
  gap: 15px;
}

/* .left-sidebar .sidebar-item .sidebar-link.active {
  background-color: var(--primary);
  color: #fff;
} */

.left-sidebar .sidebar-item .sidebar-link:hover {
  background-color: #06bbcc2e;
}

</style>
