<template>
    <Page class="page">


        <ActionBar class="action-bar" height="200" padding="0 25" BackgroundColor="#e81f1f">
            <StackLayout height="200" orientation="horizontal">
                <Image src="https://cdn.iconscout.com/icon/free/png-256/account-profile-avatar-man-circle-round-user-30452.png" width="30%" margin="0 4% 0 0"/>
                <label height="130" width = "0"/>
                <StackLayout>
                    <label class="text-left h1 font-weight-bold" :text="pageTitle" dock="bottom" verticalalignment="bottom" width="100%" height="30%" margin="25% 0 0 0"/>
                    <label class="text-left h3 font-weight-bold" text="ali98@gmail.com" dock="bottom" verticalalignment="bottom" width="100%" height="30%" margin="-20% 0 0 0"/>
                </StackLayout>
            </StackLayout>
        </ActionBar>


        <StackLayout padding="0 25">
            <StackLayout height="80%">
                <Label class="text-left h1 font-weight-bold" :text="content[0]" height="15%" Width="100%" margin="5% 0 5% 0" textWrap="true"
                    style="color: #606060;"/> 
                <label class="text-center h2" :text="content[1]" height="10%" width="100%" margin="3% 0 14% 0" /> 
                <Button class="btn btn-primary btn-rounded-lg" height="16%" width="90%" :text="buttonText[0]" @tap="$navigateTo(detailPage[0])" />
                
                <Button class="btn btn-primary btn-rounded-lg" height="16%" width="90%" :text="buttonText[1]" @tap="$navigateTo(detailPage[1])" />
            
            </StackLayout>
        </StackLayout>


        <!--StackLayout>
                <Label class="text-center h1" :text="content[0]" height="30%" Width="100%" margin="0 0 0 0" textWrap="true" />
        </StackLayout-->
    </Page>
</template>

<script>
import BuyItAgain from './9-BuyAgain'
import GrocerTracker from './10-TrackYourStock'

export default {
    data() {
      return {
        pageTitle: "Ali",
        buttonText: ["Buy it again", "Track your grocery usage"], 
        content: ["Date of purchase:" , "16 / 11 / 2018" ],
        detailPage: [BuyItAgain, GrocerTracker]
      }
    },
    methods: {

    }
}
</script>