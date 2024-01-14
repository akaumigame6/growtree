import random as r
import pygame as pg
import time
from pathlib import Path

class TaskTimer:
    def __init__(self, task_name):
        self.task_name = task_name
        self.start_time = 0
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        end_time = time.time()
        self.elapsed_time = end_time - self.start_time
        # print(f"{self.task_name} took {self.elapsed_time} seconds.")
        return self.elapsed_time

def Fib(n):
  a,b=20,30
  if n== 1:
    return a
  elif n == 2:
    return b 
  else :
    for i in range(n-2):
      a,b=b,a+b
      return b

def main():

  # 初期化処理
  pg.init() 
  pg.display.set_caption('木を育てるゲーム')
  disp_w, disp_h = 600, 300 # DisplaySize(WindowSize)
  screen = pg.display.set_mode((disp_w,disp_h)) 
  clock  = pg.time.Clock()
  font   = pg.font.Font(None,50)#フォント設定
  exit_flag = False
  exit_code = '000'

  ki1=pg.image.load("Data/ki1.png")
  ki2=pg.image.load("Data/ki2.png")
  ki3=pg.image.load("Data/ki3.png")
  ki4=pg.image.load("Data/ki4.png")
  ki5=pg.image.load("Data/ki5.png")
  kame=pg.image.load("Data/tatol.png")

  task1 = TaskTimer("Task 1")
  task1.start()
  file_path = "Data/game_data.txt"
  file_path_obj = Path(file_path)
  
  if not file_path_obj.exists():
      file_path_obj.touch()
      game_score = 0 #geme score
      Lv=0
      ki_seityou = 0
      ki_total = 1
      count=0
  else:
    with open(file_path) as f:
      l = f.readlines()
    game_score = int(l[0]) #geme score
    Lv= int(l[1])
    ki_seityou = int(l[2])
    ki_total = int(l[3])
    count= int(l[4])

  time1 = 0
  timebefor=0
  # ゲームループ [ここから]
  while not exit_flag:

    # システムイベントの検出
    for event in pg.event.get():
      if event.type == pg.QUIT: # ウィンドウ[X]の押下
        exit_flag = True
        exit_code = '001'
    ### マウスボタンイベント
      if event.type == pg.MOUSEBUTTONDOWN:#マウスクリック
        game_score+=2
        count+=2
    
    time1 = int(task1.stop())

    # 指定色で画面を塗りつぶし(fill)。実質的な画面クリア
    #screen.fill(pg.Color('BLACK'))
    screen.fill((255,255,255))

    screen.blit(font.render(f'total_point {game_score}',True,'BLACK'),(10,10))
    screen.blit(font.render(f'Lv {Lv}',True,'BLACK'),(10,60))
    screen.blit(font.render(f'total_tree {ki_total}',True,'BLACK'),(10,110))
    

    Lv=int(game_score/100)
    if Lv!=0 and time1!=timebefor:
        timebefor=time1
        if Lv<30:
          game_score+=1
          count+=1
        else:
          game_score+=int(Lv/30)
          count+=int(Lv/30)

    if count>=Fib(ki_total):
       count=0
       if ki_seityou != 4:
          ki_seityou+=1
       else :
          ki_seityou=0
          ki_total+=1

    if ki_seityou == 0:
       screen.blit(ki1,(360,130))
    elif ki_seityou == 1:
       screen.blit(ki2,(360,130))
    elif ki_seityou == 2:
       screen.blit(ki3,(360,130))
    elif ki_seityou == 3:
       screen.blit(ki4,(360,130))
    elif ki_seityou == 4:
       screen.blit(ki5,(360,130))
    screen.blit(kame,(420,200))
    # 画面出力の更新と同期
    pg.display.update()
    clock.tick(30) # 最高速度を 30フレーム/秒 に制限

  # ゲームループ [ここまで]
  l1 = [str(game_score),str(Lv),str(ki_seityou),str(ki_total),str(count)]

  with open(file_path_obj, mode='w') as f:
    f.write('\n'.join(l1))
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')