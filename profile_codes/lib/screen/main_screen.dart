import 'package:flutter/material.dart';


class MainScreen extends StatefulWidget {
  const MainScreen({Key? key}) : super(key: key);

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {

  late PageController _pageController;

  @override
  void initState(){
    super.initState();

    _pageController = PageController();
  }

  @override
  void dispose(){
    super.dispose();

    _pageController.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xff97BfB4),
        actions: [
          TextButton(onPressed: (){
            _pageController.jumpToPage(0);
          }, child: Text('HOME', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),)),
          SizedBox(width: 30.0,),
          TextButton(onPressed: (){
            _pageController.jumpToPage(1);
          }, child: Text('ABOUT', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),)),
          SizedBox(width: 30.0,),
          TextButton(onPressed: (){
            _pageController.jumpToPage(2);
          }, child: Text('SKILL', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),)),
          SizedBox(width: 30.0,),
          TextButton(onPressed: (){
            _pageController.jumpToPage(3);
          }, child: Text('CONTACT', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),)),
          SizedBox(width: 10.0,)
        ],
      ),
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        child: PageView(
          scrollDirection: Axis.vertical,
          controller: _pageController,
          children: [
            Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              decoration: BoxDecoration(
                color: Color(0xfff5eedc)
              ),
              child: Column(
                children: [
                  Expanded(
                    flex: 2,
                    child: Container(
                      child: Center(
                        child: Text('ABOUT ME', style: TextStyle(fontSize: MediaQuery.of(context).size.width/20.0, fontWeight: FontWeight.bold),),
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 8,
                    child: Container(
                      decoration: BoxDecoration(
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Expanded(
                            flex: 1,
                            child: Container(
                              child: Row(
                                mainAxisAlignment: MainAxisAlignment.end,
                                children: [
                                  Container(
                                    width: MediaQuery.of(context).size.width/4,
                                    height: MediaQuery.of(context).size.height/1.5,
                                      child: ClipRRect(
                                          child: Image.asset('assets/images/minseo.png',),
                                        borderRadius: BorderRadius.circular(10.0),
                                      ),
                                  )
                                ],
                              ),
                            ),
                          ),
                          SizedBox(width: 200.0,),
                          Expanded(
                            flex: 1,
                            child: Container(
                              width: MediaQuery.of(context).size.width/4,
                              height: MediaQuery.of(context).size.height/1.5,
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text('박민서')
                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 1,
                    child: Container(
                    ),
                  ),
                ],
              ),
            ),
            Container(
              padding: EdgeInsets.only(
                  left: 40.0,
                right: 40.0
              ),
              alignment: Alignment.center,
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              decoration: BoxDecoration(
                  color: Color(0xfff5eedc)
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text('안녕하세요! 제 이름은 박민서', style: TextStyle(fontSize: MediaQuery.of(context).size.width/20, fontWeight: FontWeight.bold),),
                  Text('모든 일에 최선을 다하는 열정적인 매니저를 꿈 꿉니다.', style: TextStyle(fontSize: MediaQuery.of(context).size.width/20, fontWeight: FontWeight.bold),),
                  SizedBox(height: 50.0,),
                  Text('Hello! My Name is Minseo Park. My dream is to be a Manager', style: TextStyle(fontSize: MediaQuery.of(context).size.width/30, fontWeight: FontWeight.bold),)
                ],
              ),
            ),
            Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              decoration: BoxDecoration(
                  color: Color(0xfff5eedc)
              ),
              child: Column(
                children: [
                  Expanded(
                    flex: 2,
                    child: Container(
                      child: Center(
                        child: Text('SKILL', style: TextStyle(fontSize: MediaQuery.of(context).size.width/20.0, fontWeight: FontWeight.bold),),
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 8,
                    child: Container(
                      decoration: BoxDecoration(
                      ),
                      child: Row(
                        children: [
                          Expanded(
                            flex: 1,
                            child: Container(
                              child: Row(
                                mainAxisAlignment: MainAxisAlignment.end,
                                children: [
                                  Container(
                                    child: ClipRRect(
                                      child: Image.asset('assets/images/minseo.png',),
                                      borderRadius: BorderRadius.circular(10.0),
                                    ),
                                  )
                                ],
                              ),
                            ),
                          ),
                          SizedBox(width: 200.0,),
                          Expanded(
                            flex: 1,
                            child: Container(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text('박민서')
                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 1,
                    child: Container(
                    ),
                  ),
                ],
              ),
            ),
            Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              decoration: BoxDecoration(
                  color: Color(0xfff5eedc)
              ),
              child: Column(
                children: [
                  Expanded(
                    flex: 2,
                    child: Container(
                      child: Center(
                        child: Text('CONTACT ME', style: TextStyle(fontSize: MediaQuery.of(context).size.width/20.0, fontWeight: FontWeight.bold),),
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 8,
                    child: Container(
                      decoration: BoxDecoration(
                      ),
                      child: Row(
                        children: [
                          Expanded(
                            flex: 1,
                            child: Container(
                              child: Row(
                                mainAxisAlignment: MainAxisAlignment.end,
                                children: [
                                  Container(
                                    child: ClipRRect(
                                      child: Image.asset('assets/images/minseo.png',),
                                      borderRadius: BorderRadius.circular(10.0),
                                    ),
                                  )
                                ],
                              ),
                            ),
                          ),
                          SizedBox(width: 200.0,),
                          Expanded(
                            flex: 1,
                            child: Container(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text('박민서')
                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 1,
                    child: Container(
                    ),
                  ),
                ],
              ),
            ),


          ],
        ),
      ),
    );
  }
}
