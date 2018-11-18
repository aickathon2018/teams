<template>
    <Page class="page">


        <ActionBar class="action-bar" height="200" padding="0 30" BackgroundColor="#e81f1f">
            <StackLayout height="200" >
                <label height="130" width = "0"/>
                <label class="text-left h1 font-weight-bold" :text="pageTitle" dock="bottom" verticalalignment="bottom" width="100%" height="30%"/>
            </StackLayout>
        </ActionBar>


        <StackLayout padding="0 25">

            <StackLayout height="12%">
                <label class="text-left h1 font-weight-bold" :text="content[0]" width="100%" height="100%" margin="20% 0 0 0"
                    style="color: #606060;"/> 
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



            <ListView for="item in listOfItems" padding="10 0" @itemTap="onItemTap" height="50%">
                <v-template>
                    <!-- Shows the list item label in the default color and style. -->
                    <StackLayout orientation="horizontal" width="100%">
                        
                        <StackLayout class="input-field" width="45%" >
                            <TextField :id="'name'+item.id" hint="Product Name" class="input" />
                            <StackLayout class="hr-light"></StackLayout>
                        </StackLayout>

                        <StackLayout class="input-field" width="30%" >
                            <TextField :id="'size'+item.id" hint="Size" class="input" />
                            <StackLayout class="hr-light"></StackLayout>
                        </StackLayout>

                        <StackLayout class="input-field" width="25%" >
                            <TextField :id="'qty'+item.id" hint="Quantity" class="input" />
                            <StackLayout class="hr-light"></StackLayout>
                        </StackLayout>

                    </StackLayout>

                </v-template>
            </ListView>   



            <img class="btn btn-primary btn-rounded-lg" src="https://cdn.iconscout.com/icon/free/png-512/plus-119-458361.png" height="64" width="64" @tap="count=count + 1; additem(count);" 
                selfalign="left"/>
            
            <StackLayout orientation="horizontal" height="8%">
                <Button class="btn btn-primary btn-rounded-lg" height="100%" width="40%" :text="buttonText[0]" @tap="$navigateTo(detailPage[0])" />
                <Button class="btn btn-primary btn-rounded-lg" height="100%" width="40%" :text="buttonText[1]" @tap="$navigateTo(detailPage[1])" />
            </StackLayout>


        </StackLayout>
    </Page>
</template>

<script>
import Back from './3-InsertReceipt'
import Next from './7-SetUpDone'

export default {
    data() {
      return {
        pageTitle: "GROCERY",
        buttonText: ["Back", "Next"], 
        content: ["LIST"],
        detailPage: [Back, Next],
        listOfItems: [
            {id: 0, text: 1}  
         ],
         count: 1
      }
    },
    methods: {
        additem(value){
            this.listOfItems.push({id: value - 1, text: value});
        }
    }
}
</script>