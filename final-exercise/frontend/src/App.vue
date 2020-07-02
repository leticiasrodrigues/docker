<template>
  <div id="app">
    <h1>E-mail Sender</h1>
    <form action="http://localhost/api" method="POST">
      <div>
        <label for="subject">Subject</label>
        <input type="text" name="subject">
      </div>
      <div>
        <label for="mensage">Message</label>
        <textarea name="mensage" rows="6" cols="50"></textarea>
      </div>
      <div>
        <button type="submit">Sent</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello world!',
    };
  },
};
</script>

<style>
.message {
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  color: blue;
}
</style>
