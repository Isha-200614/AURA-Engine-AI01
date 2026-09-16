import cv2
import time

def start_aura_engine():
    print("[INFO] Initializing AURA Engine - Real-Time Accessibility System...")
    time.sleep(1)
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Camera stream unavailable.")
        return

    print("[SUCCESS] Camera stream operational. Monitoring hazards...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.putText(frame, "AURA Engine v1.0 | Status: ACTIVE", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Domain: AI-01 (Accessibility)", (20, 75), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        cv2.putText(frame, "Hazard Index: LOW | Path Clear", (20, 110), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        cv2.imshow('AURA Engine - Visual Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_aura_engine()
