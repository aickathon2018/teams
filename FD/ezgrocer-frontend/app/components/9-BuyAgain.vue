<template>
    <Page class="page">
        <ActionBar class="action-bar" height="200" padding="0 25" BackgroundColor="#e81f1f">
            <label class="text-center h1 font-weight-bold" :text="pageTitle" dock="bottom" verticalalignment="bottom" width="100%" height="30%"/>
        </ActionBar>
        <StackLayout padding="0 25">
            <StackLayout height="21%" margin="2% 0 -4% 0">
                <label class="text-mute text-left h2" :text="content[0]" height="50%" width="100%" margin="8% 0 1% 0" textWrap="true"
                    style="color: #b8b8b8;"/> 
                    
        <!--StackLayout class="m-10" >
            <StackLayout height="13%" margin="4% 0 2% 0">
                <Label class="text-center h2" :text="content" Width="100%" textWrap="true" /-->
            </StackLayout>

            <StackLayout orientation="horizontal" height="6%" width="100%">
                                    
                <GridLayout class="input-field input-sides" width="45%" rows="auto, auto" columns="*,*">
                    <Label text="Product Name" class="label font-weight-bold" row="0" col="0" textWrap="true"/>
                </GridLayout>

                <GridLayout class="input-field input-sides" width="30%" rows="auto, auto" columns="*,*">
                    <Label text="Size" class="label font-weight-bold" row="0" col="0"  />
                </GridLayout>

                <GridLayout class="input-field input-sides" width="25%" rows="auto, auto" columns="*,*">
                    <Label text="Quan tity" class="label font-weight-bold" row="0" col="0" textWrap="true"/>
                </GridLayout>

            </StackLayout>

            <ListView for="item in listOfItems" padding="10 0" @itemTap="onItemTap" height="55%">
                <v-template>
                    <!-- Shows the list item label in the default color and style. -->
                    <StackLayout orientation="horizontal" width="100%" >
                        
                        <StackLayout class="input-field" width="45%" >
                            <TextField :text="item.name" class="input" style="color: #606060;" :isEnabled="editmou"/>
                        </StackLayout>

                        <StackLayout class="input-field" width="30%" >
                            <TextField :text="item.size" class="input" style="color: #606060;" :isEnabled="editmou" />
                        </StackLayout>

                        <StackLayout class="input-field" width="25%" >
                            <TextField :text="item.quantity" class="input" style="color: #606060;" :isEnabled="editmou" />
                        </StackLayout>

                    </StackLayout>

                </v-template>
            </ListView>   

            <StackLayout orientation="horizontal" height="20%">
                <Button class="btn btn-primary btn-rounded-lg" height="55%" width="40%" :text="buttonText[0]" @tap="editmou = !editmou"/>
                <Button class="btn btn-primary btn-rounded-lg" height="55%" width="40%" :text="buttonText[1]" @tap="$navigateTo(detailPage)" />
            </StackLayout>

        </StackLayout>
    </Page>
</template>

<script>
import Dashboard from './8-NonFirstTime'

export default {
    data() {
      return {
        pageTitle: "BUY IT AGAIN",
        buttonText: ["Edit", "Confirm"], 
        content: ["You probably have to stock up the following items" , "2999/99/99 99:99" ],
        detailPage: Dashboard,
        listOfItems: [
            {id: 0, name: "Detergent", size: "500ml", quantity: "1"} , 
            {id: 1, name: "Oil", size: "1L", quantity: "1"} , 
            {id: 2, name: "Salt", size: "500g", quantity: "1"} ,
         ],
         editmou: true,
      }
    },
    methods: {
    }
}
</script>