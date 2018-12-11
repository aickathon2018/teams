<template>
    <Page class="page">


        <ActionBar class="action-bar" height="200" padding="0 25" BackgroundColor="#e81f1f">
            <StackLayout height="200">
                <label height="130" width = "0"/>
                <label class="text-left h1 font-weight-bold" :text="pageTitle" dock="bottom" verticalalignment="bottom" width="100%" height="30%"/>
            </StackLayout>
        </ActionBar>


        <StackLayout padding="0 25">
            <StackLayout height="80%">

                <label class="text-left h1 font-weight-bold" :text="user" width="100%" height="15%" margin="5% 0 0 0"
                    style="color: #606060;"/> 
                <Label class="text-left h3" :text="content[0]" height="7%" Width="100%" margin="0% 0 10% 0" textWrap="true"
                    style="color: #606060;"/> 

                <Button class="btn btn-primary btn-rounded-lg" height="16%" width="90%" :text="buttonText[0]" @tap="$navigateTo(detailPage[0])" />
                <label class="text-center h2" :text="content[1]" height="10%" width="100%" margin="3% 0 4% 0" /> 
                <Button class="btn btn-primary btn-rounded-lg" height="16%" width="90%" :text="buttonText[1]" @tap="$navigateTo(detailPage[1])" />
            
            </StackLayout>
        </StackLayout>


        <!--StackLayout>
                <Label class="text-center h1" :text="content[0]" height="30%" Width="100%" margin="0 0 0 0" textWrap="true" />
        </StackLayout-->
    </Page>
</template>

<script>
import Next from './4-SnapReceipt'
import Next1 from './5-ManuallyInput'

export default {
    data() {
      return {
        pageTitle: "Hello,",
        user: "ALI",
        buttonText: [ "Snap your latest receipt!" , "Manually input your latest \ngrocery list/ Receipt"], 
        content: ["Set up your account with us" , "OR" ],
        detailPage: [Next, Next1]
      }
    },
    methods: {

    }
}
</script>