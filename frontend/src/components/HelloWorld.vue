<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <p>
            You're one stop shop for creating printer friendly outputs for
            battlescribe lists
        </p>

        <form enctype="multipart/form-data" method="post" name="file" action="http://192.168.180.137:8000/files/">
            <label>upload roster: </label>
            <input type="file" name="file" required/>
            <input type="submit" value="upload the roster"/>
        </form>
        <div></div>

    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from "vue-property-decorator";

    @Component
    export default class HelloWorld extends Vue {
        @Prop() private msg!: string;
    }



</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
