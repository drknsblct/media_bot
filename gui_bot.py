import time
import pyautogui


# locates image on screen
def findOnScreen():
    if pyautogui.locateOnScreen('/Users/blackout/Scraper/Gui_Bot/image/savePhoto.png', region=(2716, 562, 148, 34), confidence=0.9):
        pyautogui.press('enter')
    else:
        findOnScreen()


def photos_and_videos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # position to move
    pyautogui.click()

    for i in range(num):
        pyautogui.hotkey('command', 's')
        findOnScreen()
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.5)  # 0.5
        count += 1

    print(f'\nTotal files downloaded: {count}')


def photos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # activates browser window
    pyautogui.click()

    for i in range(num):
        pyautogui.moveTo(1063, 999)
        pyautogui.keyDown('option')
        pyautogui.click()
        pyautogui.keyUp('option')
        pyautogui.sleep(0.1)  # 0.1
        pyautogui.hotkey('command', 'w')
        count += 1

    print(f'\nTotal files downloaded: {count}')


if __name__ == '__main__':
    num = int(input('Number of open tabs: '))

    while True:
        answer = int(input('Photos[1] or Photos/Videos[2]? '))
        if answer == 1:
            start = time.time()
            photos(num)
            break
        elif answer == 2:
            start = time.time()
            photos_and_videos(num)
            break
        else:
            continue

    print(f'Time elapsed: {time.time() - start :.2f} sec.')
