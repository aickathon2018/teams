<template>
    <Page class="page">
        <ActionBar class="action-bar" height="200" padding="0 25" BackgroundColor="#e81f1f">
            <StackLayout height="200">
                <label height="130" width = "0"/>
                <label class="text-left h1 font-weight-bold" :text="pageTitle" dock="bottom" verticalalignment="bottom" width="100%" height="30%"/>
            </StackLayout>
        </ActionBar>
        <StackLayout padding="0 25">
            <StackLayout height="60%">
                <label class="text-left h1 font-weight-bold" :text="user" width="100%" height="15%" margin="5% 0 0 0"
                    style="color: #606060;"/> 
                <Label class="text-left h3" :text="content[0]" height="7%" Width="100%" margin="0% 0 0 0" textWrap="true"
                    style="color: #606060;"/> 
                <label class="text-mute text-left h2" :text="content[1]" height="18%" width="100%" margin="8% 0 3% 0" textWrap="true"
                    style="color: #b8b8b8;"/> 
                
                <DatePicker margin="0 0" height="200" verticalAlignment="center"></DatePicker>
            
            </StackLayout>
            <Button class="btn btn-primary btn-rounded-sm"  margin="2% 0 0 0" height="8%" width="80%" :text="buttonText" @tap="$navigateTo(detailPage)" />
        </StackLayout>
    </Page>
</template>

<script>
import Next from './3-InsertReceipt'

export default {
    data() {
      return {
        pageTitle: "Hello,",
        user:"ALI",
        buttonText: "Next", 
        content: ["set up your account with us" , " - When is your last shopping experience?" ],
        detailPage: Next
      }
    },
    methods: {

    }
}
</script>