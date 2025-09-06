import cv2
import numpy as np
import mss
import pyautogui

class ScreenHelper:
    def __init__(self, monitor=1, confidence=0.8):
        self.monitor = monitor
        self.confidence = confidence

    def capture_screen(self):
        with mss.mss() as sct:
            monitor = sct.monitors[self.monitor]
            img = np.array(sct.grab(monitor))
            return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    def find_image(self, template_path):
        screen = self.capture_screen()
        gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(template_path, 0)
        h, w = template.shape

        best_val = 0
        best_loc = None
        best_scale = 1.0

        # пробуем разные масштабы (0.5x до 1.5x)
        for scale in np.linspace(0.1, 1.5, 11):
            resized = cv2.resize(template, (int(w*scale), int(h*scale)))
            res = cv2.matchTemplate(gray_screen, resized, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)

            if max_val > best_val:
                best_val = max_val
                best_loc = max_loc
                best_scale = scale

        if best_val >= self.confidence:
            rw, rh = int(w * best_scale), int(h * best_scale)
            center_x = best_loc[0] + rw // 2
            center_y = best_loc[1] + rh // 2
            return (center_x, center_y, best_val)

        return None

    def click_on_image(self, template_path):
        pos = self.find_image(template_path)
        if pos:
            pyautogui.click(pos[0], pos[1])
            pyautogui.click(pos[0], pos[1])
            return True
        return False
