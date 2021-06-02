const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw new Error('Jobs is not an array')
  for (const job of jobs) {
    const newProcess = queue.create('push_notification_code_3', job)
                            .save(() => console.log(`Notification job created: ${newProcess.id}`))
    
    newProcess.on('complete', () => console.log(`Notification job ${newProcess.id} completed`))
    newProcess.on('failed', (err) => console.log(`Notification job ${newProcess.id} failed: ${err}`))
    newProcess.on('progress', (progress, data) => console.log(`Notification job ${newProcess.id} ${progress}% complete`))
  }
}

module.exports = createPushNotificationsJobs;
