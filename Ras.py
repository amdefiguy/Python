print ('==============================================')
  print ('Type 1 to Post 0 to cancel! ')
  print ('==============================================')
  post = raw_input('Do You wish To Post ? ')  
  if post == 1:
      graph.put_object("me", "feed", message=msg)
  else:
      print ('Bye, Sure Do Come Back!')