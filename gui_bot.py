import pyautogui
import time


def photos_and_videos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # position to move
    pyautogui.click()

    for i in range(num):
        pyautogui.hotkey('command', 's')
        pyautogui.sleep(1.5) #1.5
        pyautogui.press('enter')
        pyautogui.sleep(0.5) #0.5
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.5) #0.5
        count += 1

    print(f'\nTotal files downloaded: {count}')


def photos(num):
    count = 0
    pyautogui.moveTo(60, 60)  # activates browser window
    pyautogui.click()

    for i in range(num):
        pyautogui.moveTo(1063, 999)
        pyautogui.click()
        pyautogui.sleep(1) #wait for webpage to open
        pyautogui.hotkey('command', 's')
        pyautogui.sleep(1.5) #2
        pyautogui.press('enter')
        pyautogui.sleep(0.1)
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.1)
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(0.1)
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


