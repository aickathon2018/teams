<template>
    <Page class="page">
        <actionBar title=""/>
        <FlexboxLayout flexDirection="column-reverse" alignItems="stretch">
            <Button class="btn btn-primary btn-rounded-lg" height="8%" width="60%" margin="0 10% 3%" :text="buttonText" @tap="$navigateTo(detailPage)" />
            <StackLayout height="80%">
                <label height="40%" width="0"/> 
                <Label class="text-center h2" :text="content" textWrap="true" verticalAlignment="center" height="40%" minWidth="100%" 
                    style="color: #b8b8b8;"/>
            </StackLayout>
        </FlexboxLayout>
    </Page>
</template>

<script>
import Dashboard from './8-NonFirstTime'

export default {
    data() {
      return {
        pageTitle: "Set up Successful!",
        buttonText: "Check your dashboard",
        content: "You have successfully set up your account!",
        detailPage: Dashboard
      }
    },
    methods: {

    }
}
</script>