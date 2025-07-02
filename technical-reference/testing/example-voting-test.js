/**
 * Example: Disability Justice Testing for DRUIDS Voting System
 * 
 * This example demonstrates how to write tests that center
 * disabled users' actual experiences rather than technical compliance.
 */

import { 
  getCommunityTesters, 
  createTestUser,
  measureRealOutcomes 
} from '@druids/disability-justice-testing';

describe('Democratic Centralist Voting - Disability Justice Tests', () => {
  // Recruit actual disabled users as paid testers
  const communityTesters = getCommunityTesters({
    disabilities: [
      'blind-screen-reader',
      'low-vision-magnification',
      'motor-speech-recognition',
      'adhd-executive-dysfunction',
      'chronic-fatigue',
      'autism-sensory-sensitivity'
    ],
    compensation: '$150/hour',
    timeframe: 'crip-time-respected'
  });

  describe('Proposal Comprehension', () => {
    test.each(communityTesters)(
      '%s can understand proposal within their normal timeframe',
      async (tester) => {
        const proposal = await loadProposal('abolish-police-funding');
        const startTime = Date.now();
        
        const comprehension = await tester.reviewProposal(proposal);
        const timeSpent = Date.now() - startTime;
        
        // Success = understanding, not speed
        expect(comprehension.understoodMainPoints).toBe(true);
        expect(comprehension.identifiedImplications).toBe(true);
        expect(comprehension.feltRushed).toBe(false);
        
        // No arbitrary time limits
        expect(proposal.hasDeadline).toBe(false);
      }
    );
  });

  describe('Voting Process Accessibility', () => {
    test('screen reader user can vote without sighted assistance', async () => {
      const voter = await createTestUser({
        screenReader: 'NVDA',
        visualAcuity: 'totally-blind'
      });
      
      const votingFlow = await voter.navigateToVoting();
      
      // Every step must be independently verifiable
      expect(votingFlow.foundVotingSection).toBe(true);
      expect(votingFlow.heardProposalSummary).toBe(true);
      expect(votingFlow.understoodOptions).toEqual(['yes', 'no', 'abstain']);
      expect(votingFlow.confirmedSelection).toBe(true);
      expect(votingFlow.receivedConfirmation).toBe(true);
      
      // No vision-dependent steps
      expect(votingFlow.requiredVisualVerification).toBe(false);
    });

    test('user with hand tremors can vote accurately', async () => {
      const voter = await createTestUser({
        motorControl: 'essential-tremor',
        preferredInput: 'mouse'
      });
      
      const targets = await voter.getInteractiveElements();
      
      targets.forEach(target => {
        // Large touch targets for imprecise movement
        const size = target.getBoundingBox();
        expect(size.width).toBeGreaterThanOrEqual(44);
        expect(size.height).toBeGreaterThanOrEqual(44);
        
        // Confirmation before irreversible actions
        if (target.isIrreversible()) {
          expect(target.hasConfirmationStep).toBe(true);
          expect(target.confirmationIsAccessible).toBe(true);
        }
      });
      
      // Ability to correct mistakes
      expect(voter.canChangeVoteBeforeSubmit).toBe(true);
    });

    test('user with ADHD can maintain focus through voting', async () => {
      const voter = await createTestUser({
        cognitiveProfile: 'adhd-inattentive',
        workingMemorySupport: 'needed'
      });
      
      const interface = await voter.getVotingInterface();
      
      // Persistent context
      expect(interface.proposalAlwaysVisible).toBe(true);
      expect(interface.progressIndicatorPresent).toBe(true);
      expect(interface.canReviewPreviousSteps).toBe(true);
      
      // No cognitive overload
      const choices = interface.getSimultaneousChoices();
      expect(choices.length).toBeLessThanOrEqual(5);
      
      // Clear navigation
      expect(interface.breadcrumbsVisible).toBe(true);
      expect(interface.nextStepExplicit).toBe(true);
    });
  });

  describe('Asynchronous Participation', () => {
    test('chronic illness user can participate despite flares', async () => {
      const participant = await createTestUser({
        chronicIllness: 'me-cfs',
        energyPattern: 'unpredictable'
      });
      
      // Start voting process
      await participant.beginVoting();
      await participant.fillPartialBallot(30); // 30% complete
      
      // Simulate symptom flare requiring rest
      await participant.simulateFlare();
      await participant.rest({ hours: 48 });
      
      // Can resume exactly where left off
      const resumed = await participant.resumeVoting();
      expect(resumed.progressPreserved).toBe(true);
      expect(resumed.contextRestored).toBe(true);
      expect(resumed.noDeadlinePressure).toBe(true);
    });
  });

  describe('Privacy with Accessibility', () => {
    test('voting remains private with assistive technology', async () => {
      const voter = await createTestUser({
        assistiveTech: ['screen-reader', 'voice-input']
      });
      
      const privacyMeasures = await voter.checkPrivacy();
      
      // Assistive tech doesn't compromise privacy
      expect(privacyMeasures.screenReaderAnnouncements)
        .not.toBeAudibleToOthers();
      expect(privacyMeasures.voiceCommandsProcessedLocally)
        .toBe(true);
      expect(privacyMeasures.noAssistiveTechLogging)
        .toBe(true);
    });
  });

  describe('Error Recovery', () => {
    test('errors are recoverable and understandable', async () => {
      const voter = await createTestUser({
        cognitiveLoad: 'easily-overwhelmed'
      });
      
      // Simulate common error
      await voter.makeError('invalid-selection');
      
      const errorHandling = voter.getErrorExperience();
      
      expect(errorHandling.errorMessageClear).toBe(true);
      expect(errorHandling.solutionProvided).toBe(true);
      expect(errorHandling.progressNotLost).toBe(true);
      expect(errorHandling.noShamingLanguage).toBe(true);
      expect(errorHandling.canGetHelp).toBe(true);
    });
  });

  describe('Real Outcomes Measurement', () => {
    test('measure actual participation rates by disability', async () => {
      const metrics = await measureRealOutcomes({
        feature: 'voting-system',
        period: '3-months',
        demographics: 'collect-disability-status'
      });
      
      // Success = equitable participation
      const participationByDisability = metrics.getParticipationRates();
      const overallRate = metrics.getOverallRate();
      
      Object.entries(participationByDisability).forEach(([disability, rate]) => {
        // No group left behind
        expect(rate).toBeGreaterThan(overallRate * 0.8);
      });
      
      // Identify and address barriers
      const barriers = metrics.getReportedBarriers();
      expect(barriers).toBeActionable();
      expect(barriers).toBeAddressedInNextSprint();
    });
  });
});

/**
 * Community Validation Integration
 * 
 * These tests don't pass until reviewed by community
 */
describe.community('Community-Validated Voting Tests', () => {
  const reviewers = assignCommunityReviewers({
    expertise: 'voting-accessibility',
    compensation: 'standard-rate'
  });
  
  test.requiresApproval('voting system meets community needs', {
    reviewers,
    criteria: {
      'actually-usable': true,
      'dignity-preserving': true,
      'culturally-appropriate': true,
      'trauma-informed': true
    }
  });
});