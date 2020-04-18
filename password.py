print('Enter ')
                        print(type(str(text1)))

                        if text1 == pf:
                            print('password matched')
                            data.write(str.encode('1'))
                            text1=[]
                            count=0
                            once =1
##                            pf = Rfid_scanner()
                        else:
                            print('not matched ')
                            data.write(str.encode('2'))
                            client = Client(account_sid, auth_token)

                            client.api.account.messages.create(
                                to="+91-9481331250",
                                from_="+1 202-740-9449" ,  #+1 210-762-4855"
                                body=" Pasword mismach" )

                            text1=[]
                            count=0
##                        if text == 'AZ':
##                            print('password matches ')
##                    sound.play()
                    select_keyboard_menu = True
