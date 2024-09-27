Feature: Sample Integration Consumer

  @stage @qa
  Scenario: When a product is updated, it is checked that an product-domain-topic event is received for the related topic
    Given I set "ProductUpdatedEvent" kafka message document
    Given I start kafka consumer for topic "product-integration-topic" with "product-consumer-group-journey" group name
    When I send message to kafka "product-domain-topic" topic
    Then I should see "product-integration-topic" event on "product-consumer-group-journey" group name in kafka