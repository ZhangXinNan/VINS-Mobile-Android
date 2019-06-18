
mainLoop_isCancelled            ->  run()
globalLoopThread_isCancelled    ->  globalPoseGraphLoop
saveData_isCancelled            ->  saveDataLoop/saveDataLoopImu
loop_thread_isCancelled         ->  loopDetectionLoop

viewDidLoad()                   ->  imuStartUpdate()
onPause()                       ->  imuStopUpdate()